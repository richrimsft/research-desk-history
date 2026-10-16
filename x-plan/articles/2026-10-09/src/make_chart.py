import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
sp=2.2255;ts=1.5286;comb=sp+ts;deficit=2.0
labels=['SpaceX\n(SPCX)','Tesla\n(TSLA)','SpaceX +\nTesla','FY2026\nfederal deficit']
vals=[sp,ts,comb,deficit]
colors=['#4C9BE8','#E8504C','#B57BFF','#9AA0A6']
fig,ax=plt.subplots(figsize=(12,12),dpi=150)
fig.patch.set_facecolor('#0f1115'); ax.set_facecolor('#0f1115')
b=ax.bar(labels,vals,color=colors,width=0.62)
for r,v in zip(b,vals):
    ax.text(r.get_x()+r.get_width()/2,v+0.06,f'${v:.2f}T',ha='center',va='bottom',color='white',fontsize=30,fontweight='bold')
ax.set_ylim(0,4.4); ax.set_yticks([0,1,2,3,4])
ax.tick_params(axis='x',colors='white',labelsize=22,length=0)
ax.tick_params(axis='y',colors='#9AA0A6',labelsize=16)
ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x,p:f'${x:.0f}T'))
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#444')
ax.grid(axis='y',color='#2a2d33',linewidth=1); ax.set_axisbelow(True)
fig.suptitle('Two Musk companies vs. one year of deficit',color='white',fontsize=34,fontweight='bold',y=0.965)
ax.set_title(f'Market caps vs. the FY2026 U.S. federal deficit. Combined is {comb/deficit:.2f}x.',color='#C9CDD2',fontsize=20,pad=18)
fig.text(0.5,0.025,'Sources: Nasdaq.com market caps as of Oct 9, 2026, 10:36am ET; FY2026 deficit: CBO via CRFB (Oct 8, 2026)',ha='center',color='#9AA0A6',fontsize=14)
plt.tight_layout(rect=(0,0.05,1,0.93))
fig.savefig('chart.png',facecolor=fig.get_facecolor())
print(comb, comb/deficit)
