from modules import file_handler as fh, match_result_engine as mre
from modules.sortable_class import Sortable

test_list = fh.load("test")


for test in test_list:
	test.print()

mre.resolve_duel(test_list[2],test_list[0],False)

for test in test_list:
	test.print()
