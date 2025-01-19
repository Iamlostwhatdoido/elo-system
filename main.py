import ui
from modules import file_handler as fh, match_result_engine as mre
from modules.sortable_class import Sortable

def test_ui():
	ui.start_ui()

def basic_duel():
	sortable_list = fh.load('test')
	chosen_two = sortable_list[35:37]

	for sortable in chosen_two:
		sortable.display()
	
	mre.resolve_match([chosen_two[0]],[chosen_two[1]])

	for sortable in chosen_two:
		sortable.display()


if __name__ == "__main__":
	test_ui()
