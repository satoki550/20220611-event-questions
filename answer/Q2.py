def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    mid_point=int(len(sorted_array)/2)
    target_index=mid_point
    while True:
        mid_point=int(len(sorted_array)/2)
        if sorted_array[mid_point]>target_number:
            sorted_array=sorted_array[:mid_point]
            target_index=int(len(sorted_array)/2)
        elif sorted_array[mid_point]<target_number:
            sorted_array=sorted_array[mid_point:]
            target_index=mid_point+int(len(sorted_array)/2)
        else:
            if sorted_array[mid_point]==target_number:
                return target_index
            else:
                break

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1
  
  if __name__=='__main__':
    main()
