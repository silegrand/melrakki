import pymupdf as fitz
LIB='/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
PLEX='/mnt/skills/examples/canvas-design/canvas-fonts/IBMPlexMono-Regular.ttf'
SRC='/home/claude/site/original-backup/'
def find(page, text):
    for b in page.get_text('dict')['blocks']:
        for l in b.get('lines',[]):
            for s in l['spans']:
                if s['text']==text: return s
    raise SystemExit('not found: '+text)
def bg(page, r):
    pm=page.get_pixmap(clip=fitz.Rect(r.x0-4, r.y0, r.x0-1, r.y1), dpi=72)
    c=pm.pixel(0, pm.height//2); return tuple(v/255 for v in c[:3])
def hexcol(c): return ((c>>16)&255)/255, ((c>>8)&255)/255, (c&255)/255
def edit(doc, pno, old, new, lines=1, width=None, drop=False):
    p=doc[pno]; s=find(p,old); r=fitz.Rect(s['bbox'])
    fill=bg(p,r)
    p.add_redact_annot(r+(-0.5,-0.5,0.5,0.5), fill=False); p.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE, graphics=fitz.PDF_REDACT_LINE_ART_NONE)
    if drop: return
    font=PLEX if 'Plex' in s['font'] else LIB
    name='plexm' if font==PLEX else 'libs'
    size=s['size']; col=hexcol(s['color'])
    box=fitz.Rect(r.x0, r.y0, r.x0+(width or 500), r.y0+size*1.3*lines+4)
    rc=p.insert_textbox(box, new, fontsize=size, fontfile=font, fontname=name, color=col, lineheight=1.18)
    if rc<0: raise SystemExit(f'OVERFLOW {old} {rc}')
d=fitz.open(SRC+'Melrakki-Harka-Solar.pdf')
edit(d,0,'Fuel-free monitoring on hazardous sites.','Fuel-free monitoring for remote oil, gas and mining sites.',lines=2,width=160)
edit(d,0,'Silent, no thermal or acoustic signature.','Silent, no engine heat or exhaust.')
edit(d,1,'Silent at all times, with no exhaust and no thermal signature.','Silent at all times, with no engine heat or exhaust.')
edit(d,1,'01227 202122','',drop=True)
edit(d,1,'Manufactured in Italy to Melrakki Systems specification. Specifications, items and design may be modified','Manufactured to Melrakki Systems designs and specifications. Specifications, items and design may be modified')
d.subset_fonts(); d.save('Melrakki-Harka-Solar.pdf',garbage=3,deflate=True)
h=fitz.open(SRC+'Melrakki-Harka-Hybrid.pdf')
edit(h,0,'Generator engages at 20% depth of discharge and shuts down','Generator engages at 40% state of charge and shuts down')
edit(h,0,'45 h','41 h')
edit(h,1,'45 hrs','41 hrs')
edit(h,1,'at 20% depth of discharge to recharge the pack, then stops.','at 40% state of charge to recharge the pack, then stops.')
edit(h,1,'01227 202122','',drop=True)
edit(h,1,'Manufactured in Italy to Melrakki Systems specification. Specifications, items and design may be modified','Manufactured to Melrakki Systems designs and specifications. Specifications, items and design may be modified')
h.subset_fonts(); h.save('Melrakki-Harka-Hybrid.pdf',garbage=3,deflate=True)
out='/tmp/claude-0/-home-claude/5bb972ba-40bb-5aa1-a697-0b0ebb37f463/scratchpad/shots/'
d=fitz.open('Melrakki-Harka-Solar.pdf')
for i,clip in [(0,(200,700,560,770)),(1,(20,560,580,830))]: d[i].get_pixmap(dpi=150,clip=fitz.Rect(*clip)).save(out+f'sol2_{i}.png')
h=fitz.open('Melrakki-Harka-Hybrid.pdf')
for i,clip in [(0,(20,370,330,630)),(1,(300,90,580,560)),(1,(20,740,580,830))]: h[i].get_pixmap(dpi=110,clip=fitz.Rect(*clip)).save(out+f'hyb2_{i}_{clip[1]}.png')
print('ok')
