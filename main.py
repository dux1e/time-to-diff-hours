from datetime import datetime, timedelta
import argparse
import locale
import pyperclip

def calc_time_diff(from_time: int, to_time: int, pause_minutes: int) -> str:
    from_str = f'{from_time:04d}'
    to_str = f'{to_time:04d}'
    
    form_time_obj = datetime.strptime(from_str, '%H%M').time()
    to_time_obj = datetime.strptime(to_str, '%H%M').time()
    
    from_datetime = datetime.combine(datetime.min, form_time_obj)
    to_datetime = datetime.combine(datetime.min, to_time_obj)
    
    time_diff = to_datetime - from_datetime
    
    time_diff -= timedelta(minutes=pause_minutes)    
    
    hours_decimal = time_diff.total_seconds() / 3600
    
    locale.setlocale(locale.LC_NUMERIC, 'da_DK.UTF-8')
    
    hours_decimal = locale.format_string('%.2f', hours_decimal, grouping=True)
    pyperclip.copy(hours_decimal)
    
    return hours_decimal

def main():
    parser = argparse.ArgumentParser(description='Calculate time difference in decimal hours')
    parser.add_argument('-f', '--fromtime', type=int, help='From time in HHMM format')
    parser.add_argument('-t', '--totime', type=int, help='To time in HHMM format')
    parser.add_argument('-p', '--pauseminutes', type=int, help='Minutes to subtract', default=0, nargs='?')
    
    args = parser.parse_args()
    
    decimal_hours = calc_time_diff(args.fromtime, args.totime, args.pauseminutes)
    
    print(f'Time difference in decimal hours: {decimal_hours}')
    

if __name__ == '__main__':
    main()
