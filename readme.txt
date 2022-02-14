If you have no OpenCV and matplotlib, install them (I also install them with PyCharm's to click right "Show Context Actions").
My environment is Python 3.9.2

1: Paste your pictures into "input".
2: Open the terminal at this project directory.
3: Type "python main.py".
4: Converted files will be created into "output" (JPG -> PNG, PNG -> JPG).



### MEMO

OpenCV(4.5.5) D:\a\opencv-python\opencv-python\opencv\modules\imgproc\src\color.cpp:182: error: (-215:Assertion failed) !_src.empty() in function
The cause was that original pictures title was Japanese. Convert succeeded after renamed them English.