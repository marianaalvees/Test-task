from sync import compare_sync_folders

source_path = "C:\\Users\\maria\\Documents\\Others\\Test-task\\source"
replica_path = "C:\\Users\\maria\\Documents\\Others\\Test-task\\replica"
log = "C:\\Users\\maria\\Documents\\Others\\Test-task\\log"
compare_sync_folders(source_path, replica_path, 20, log)
