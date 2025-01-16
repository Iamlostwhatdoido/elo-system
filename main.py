from modules import file_handler as fh







test_list = fh.load("test")

for test in test_list:
	test.print(show_image_path=True)