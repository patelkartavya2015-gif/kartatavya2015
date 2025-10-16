def shut_downOperations():
    function = str(input("Are any application on?(y/n): "))
    sure = str(input("Are you sure you want to shut down?(y/n): "))
    if function == "n" and sure == "y":
        print("Shutting down...")
    else:
        print("Shut down cancelled due to applications running or user cancellation.")
    return

print("starting shut down operations...\n")
shut_downOperations()
