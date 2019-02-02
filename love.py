love="i love you too."
heart=input("어필하시오\n") #어필을해주세요 ex>널 평생 사랑해,사랑해,사랑합니다.
heart=[print(love+str(say)+"세") for say in range(20,101) if "사랑" in heart]
print("평생사랑했습니다.")
