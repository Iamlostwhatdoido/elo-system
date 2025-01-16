from modules import file_handler as fh, match_result_engine as mre







test_list = fh.load("test")

for test in test_list:
	test.print(show_image_path=True)