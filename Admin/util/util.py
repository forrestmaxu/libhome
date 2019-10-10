def dig_to_ch(num):
    dig=['零','一', '二', '三', '四', '五', '六', '七', '八', '九' ]
    units=['', '十', '百', '千', '万', '十', '百', '千', '亿' ]
    unit=0
    result=[]
    while num!=0:      
        number=num%10
        if number!=0:
            result.insert(0,units[unit])
        # print(dig[number])
        result.insert(0,dig[number])
        unit+=1
        num=num/10
        num=int(num)
    result=''.join(result)
    result="第"+result+"条"
    return result


if __name__ == "__main__":
    print(dig_to_ch(107))