from modules import file_handler as fh








if __name__ == "__main__":
	test_list = fh.load("test")

	for test in test_list:
		test.print(show_image_path=True)