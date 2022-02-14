If you have no OpenCV and matplotlib, install them (I also install them with PyCharm's to click right "Show Context Actions").
My environment is Python 3.9.2


COPY and paste your pictures into "input". Do not CUT and paste. It needs to remain original files in another directory. Because if original files include multi bytes chars, they will be renamed automatically.

Open the terminal at this project directory.

Type "python main.py".

Converted files will be created into "output" (JPG -> PNG, PNG -> JPG).



### MEMO

OpenCV(4.5.5) D:\a\opencv-python\opencv-python\opencv\modules\imgproc\src\color.cpp:182: error: (-215:Assertion failed) !_src.empty() in function
The cause was that original pictures title was Japanese. Convert succeeded after renamed them English.
Added function that removing multi bytes characters from original files in "input" directory.