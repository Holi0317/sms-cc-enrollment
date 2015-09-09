#sms-cc-enrollment
Computer club 2015-2016 enrollment day Q&A program

## 簡介
2小時內隨便做出來的鬼東西 ;p

## 安裝
1. 需要Python3
2. 執行 `pip install git+git://github.com/holi0317/sms-cc-enrollment.git@v1.1.2`
3. 執行 `enrollment`
4. (建議) 執行 `while true;do enrollment && exit; done`

## Troll
提供謀殺這程式的方法, 因為大部份(除了 KILLSIG 9以外)關閉這程式的方法也不能使用.

## 設定
{
  "troll": true, # 開啟troll模式
  "max_attempt": 3,
  "questions": [
    {
      "question": "foo",
      "ignore_case": true,
      "answer": "bar",
      "hint": "The answer is bar"
    },
    {
      "question": "foo2",
      "ignore_case": true,
      "answer": "bar2",
      "hint": "The answer is bar2"
    }
  ]
}
