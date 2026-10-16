import subprocess, sys, math
from PIL import Image, ImageFilter
from multiprocessing import Pool
D=[4,4,3,4,3,3,4,2,3,3,3,5,5,5,4,5]; X=1.5; S=2592; O=2160; FPS=30
def ease(t): return t*t*(3-2*t)
def seg(i):
    src=Image.open(f"up/raw_s{i+1:02d}.png").convert("RGB").resize((S,S),Image.LANCZOS)
    src=src.filter(ImageFilter.UnsharpMask(radius=1.2,percent=40,threshold=2))
    L=D[i]+X if i<15 else 6.5; n=round(L*FPS)
    m=i%4  # 0 push-in,1 pull-out+pan right,2 push-in+pan up,3 pull-out+pan left
    p=subprocess.Popen(["ffmpeg","-y","-v","error","-f","rawvideo","-pix_fmt","rgb24","-s",f"{O}x{O}","-r",str(FPS),"-i","-","-c:v","libx264","-preset","fast","-crf","10","-pix_fmt","yuv420p",f"seg/s{i:02d}.mp4"],stdin=subprocess.PIPE)
    for f in range(n):
        e=ease(f/(n-1))
        z = 1+0.13*e if m in (0,2) else 1.13-0.13*e
        z=max(z,1.0); vw=S/z; margin=max(S-vw,0.0)
        px=0.5; py=0.5
        if m==1: px=0.35+0.3*e
        if m==3: px=0.65-0.3*e
        if m==2: py=0.6-0.2*e
        x0=margin*px; y0=margin*py
        p.stdin.write(src.resize((O,O),Image.BICUBIC,box=(x0,y0,x0+vw,y0+vw)).tobytes())
    p.stdin.close(); p.wait(); return i,n
if __name__=="__main__":
    import os; os.makedirs("seg",exist_ok=True)
    if "--skip" not in sys.argv:
        with Pool(3) as pl: print(pl.map(seg,range(16)))
    ins=[];fl=[]
    for i in range(16): ins+=["-i",f"seg/s{i:02d}.mp4"]; fl.append(f"[{i}:v]setsar=1,setpts=PTS-STARTPTS,fps=30[v{i}]")
    prev="v0";off=0;tr=["fade","fade","smoothleft","fade","fade","smoothright","fade","fade","fade","fade","fade","smoothleft","fade","fade","fade"]
    for i in range(1,16):
        off+=D[i-1]
        fl.append(f"[{prev}][v{i}]xfade=transition={tr[i-1]}:duration={X}:offset={off-0.25}[x{i}]");prev=f"x{i}"
    F="/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"; k=3
    t1=f"drawtext=fontfile={F}:text='THE FALL OF THE DARK EMPIRE':fontsize={30*k}:fontcolor=white:shadowcolor=black:shadowx={2*k}:shadowy={2*k}:x=(w-tw)/2:y=h-{110*k}:enable='between(t,0.5,3.6)':alpha='if(lt(t,1.2),(t-0.5)/0.7,if(gt(t,3),(3.6-t)/0.6,1))'"
    t2=f"drawtext=fontfile={F}:text='the cycle never breaks':fontsize={40*k}:fontcolor=0xD8D8D8:x=(w-tw)/2:y=(h-th)/2:enable='between(t,61,63.2)':alpha='if(lt(t,61.6),(t-61)/0.6,if(gt(t,62.6),(63.2-t)/0.6,1))'"
    t3=f"drawtext=fontfile={F}:text='@P7RIM3':fontsize={46*k}:fontcolor=0xC8102E:x=(w-tw)/2:y=(h-th)/2:enable='between(t,63.3,64.95)':alpha='if(lt(t,63.8),(t-63.3)/0.5,1)'"
    fl.append(f"[{prev}]trim=duration=61,fade=t=out:st=60:d=1,tpad=stop_mode=add:stop_duration=4:color=black,{t1},{t2},{t3},trim=duration=64.95,format=yuv420p[vout]")
    subprocess.run(["ffmpeg","-y","-v","error",*ins,"-i","part2_final.mp4","-filter_complex",";".join(fl),"-map","[vout]","-map","16:a","-c:a","copy","-c:v","libx264","-preset","slow","-profile:v","high","-crf","16","-r","30","-movflags","+faststart","part2_4k.mp4"],check=True)
