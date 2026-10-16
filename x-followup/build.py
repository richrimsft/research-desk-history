import subprocess
D=[4,4,3,4,3,3,4,2,3,3,3,5,5,5,4,5]
F="/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
ins=[];fl=[]
for i,d in enumerate(D):
    L=d+1 if i<15 else 6
    n=L*30
    ins+=["-i",f"stills/s{i+1:02d}.png"]
    fl.append(f"[{i}:v]scale=1440:1440,zoompan=z='1+0.0008*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=720x720:fps=30,setsar=1,format=yuv420p,trim=duration={L},setpts=PTS-STARTPTS,fps=30[v{i}]")
prev="v0";off=0
for i in range(1,16):
    off+=D[i-1]
    fl.append(f"[{prev}][v{i}]xfade=transition=fade:duration=1:offset={off-0.5 if False else off}[x{i}]");prev=f"x{i}"
t1="drawtext=fontfile=%s:text='THE FALL OF THE DARK EMPIRE':fontsize=30:fontcolor=white:shadowcolor=black:shadowx=2:shadowy=2:x=(w-tw)/2:y=h-110:enable='between(t,0.5,3.6)':alpha='if(lt(t,1.2),(t-0.5)/0.7,if(gt(t,3),(3.6-t)/0.6,1))'"%F
t2="drawtext=fontfile=%s:text='the cycle never breaks':fontsize=40:fontcolor=0xD8D8D8:x=(w-tw)/2:y=(h-th)/2:enable='between(t,61,63.2)':alpha='if(lt(t,61.6),(t-61)/0.6,if(gt(t,62.6),(63.2-t)/0.6,1))'"%F
t3="drawtext=fontfile=%s:text='@P7RIM3':fontsize=46:fontcolor=0xC8102E:x=(w-tw)/2:y=(h-th)/2:enable='between(t,63.3,64.95)':alpha='if(lt(t,63.8),(t-63.3)/0.5,1)'"%F
fl.append(f"[{prev}]fade=t=out:st=60:d=1,tpad=stop_mode=add:stop_duration=5:color=black,{t1},{t2},{t3},trim=duration=64.95[vout]")
subprocess.run(["ffmpeg","-y","-v","error",*ins,"-filter_complex",";".join(fl),"-map","[vout]","-c:v","libx264","-preset","medium","-crf","19","-pix_fmt","yuv420p","-r","30","video.mp4"],check=True)
