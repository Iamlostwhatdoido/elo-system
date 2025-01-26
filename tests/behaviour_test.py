from modules import match_result_engine as mre
from modules.sortable_class import Sortable

def run():
	
	strong_unclear 	= lambda : Sortable("Strong & Unclear",	300,	400,"")
	mid_unclear 	= lambda : Sortable("Mid & Unclear",	0,		400,"")
	weak_unclear 	= lambda : Sortable("Weak & Unclear",	-300,	400,"")
	strong_known 	= lambda : Sortable("Strong & Known",	300,	200,"")
	mid_known 		= lambda : Sortable("Mid & Known",		250,		200,"")
	weak_known 		= lambda : Sortable("Weak & Known",		-300,	200,"")
	strong_precise 	= lambda : Sortable("Strong & Precise",	300,	50,"")
	mid_precise 	= lambda : Sortable("Mid & Precise",	0,		50,"")
	weak_precise 	= lambda : Sortable("Weak & Precise",	-300,	50,"")

	roster = [strong_unclear, mid_unclear,weak_unclear,strong_known,mid_known,weak_known,strong_precise,mid_precise,weak_precise]

	# for _ in range(10):
	# 	print("\n\n NEW MATCH !")
	# 	sample = random.sample(roster,2)
	# 	mre.resolve_match([sample[0]()],[sample[1]()],True)

	mre.resolve_match([weak_precise()],[weak_unclear()],True)
	mre.resolve_match([weak_precise()],[weak_known()],True)
	mre.resolve_match([weak_precise()],[weak_precise()],True)