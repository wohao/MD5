import hashlib
import base64

source = "NDRiMWZmMmVjZTk5MTFjMWI1MDNkYTY0MzZlYTAzMTA=\n"

datas = {"我们在一起吧","我选择原谅你","别说话，吻我","多喝热水"}
for data in datas:

	dataout = hashlib.md5(data.encode("utf-8")).hexdigest()
	result = (base64.encodestring(dataout.encode("utf-8"))).decode("utf-8")

	if (result == source):
		print("答案是：",data)





