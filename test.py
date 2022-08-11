import pandas as pd
import chardet
import itertools
# with open('./src/text.txt', 'r', encoding='utf-8') as f:
#     data = f.read()
#     df = pd.DataFrame(data.split('\n'), columns=["Content"])
#     df.to_csv('content.csv', index = False, encoding='utf-8-sig')
#     print(chardet.detect(str.encode(df.iloc[0]["Content"])))
#     for c in df.iloc[0]["Content"]:
#         print(c)
#         print(ord(c))
squirrel = {0 : ["吱", "喳", "嘰"],
            1 : ["吱吱", "吱喳", "吱嘰", "喳吱", "喳喳", "喳嘰", "嘰吱", "嘰喳", "嘰嘰"],
            2 : ["吱吱吱", "吱吱喳", "吱吱嘰", "吱喳吱", "吱喳喳", "吱喳嘰", "吱嘰吱", "吱嘰喳", "吱嘰嘰", "喳吱吱", "喳吱喳", "喳吱嘰", "喳喳吱", "喳喳喳", "喳喳嘰", "喳嘰吱", "喳嘰喳", "喳嘰嘰", "嘰吱吱", "嘰吱喳", "嘰吱嘰", "嘰喳吱", "嘰喳喳", "嘰喳嘰", "嘰嘰吱", "嘰嘰喳", "嘰嘰嘰"]}
print(len(squirrel[2]))