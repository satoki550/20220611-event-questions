def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]
    
    # ここから記述
    array_tmp=array.copy()
    for i in range(0,len(array)):
        for j in range(1,len(array)+1):
            if pivot>array[i]:
                break
            if pivot<=array[i] and pivot>array[-j]:
                array[i]=array_tmp[-j]
                array[-j]=array_tmp[i]
                array_tmp=array.copy()
                break
            if i+j>=len(array):
                if i==0 or j==0:
                    return array
                return sort(array[:i])+sort(array[-j:])
                continue
            
    # ここまで記述

if __name__ == '__main__':
    main()
