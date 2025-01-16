from modules import file_handler as fh, match_result_engine as mre
from modules.sortable_class import Sortable

strong_precise = Sortable("Strong & Precise",500,50,None)
strong_unclear = Sortable("Strong & Unclear",500,400,None)
weak_precise = Sortable("Weak & Precise",-500,50,None)
weak_unclear = Sortable("Weak & Unclear",-500,400,None)

mre._average([strong_precise,strong_unclear]).print()



test_list = fh.load("test")

for test in test_list:
	test.print(show_image_path=True)