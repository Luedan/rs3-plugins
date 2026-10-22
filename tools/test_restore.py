import sys
sys.path.append(r'D:\programacion\REPOS\rs-plugins\runescape-dialogue-translator\scripts')
import restore_conditions

total_files, modified_files, total_lines = restore_conditions.process_all()
print(f"Result: total={total_files}, modified={modified_files}, lines={total_lines}")
