start_sum = float(input())
percent_sum = float(input())
target_sum = float(input())
month_count = 0
while start_sum < target_sum:
    start_sum += start_sum * (percent_sum / 100) / 12
    month_count += 1
    print(f'{month_count} - {start_sum:.2f}')




