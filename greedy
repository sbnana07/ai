def printJobScheduling(arr, t):
    # length of array
    n = len(arr)

    # Sort all jobs according to decreasing order of profit
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # To keep track of free time slots
    result = [False] * t

    # To store result (Sequence of jobs)
    job = ['-1'] * t

    total_profit = 0  # Initialize total profit to 0

    # Iterate through all given jobs
    for i in range(len(arr)):
        # Find a free slot for this job
        # (Note that we start from the last possible slot)
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            # Free slot found
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                total_profit += arr[i][2]  # Add profit of the scheduled job
                break

    # print the sequence and maximum profit
    print(f"Job Sequence: {job}")
    print(f"Maximum Profit: {total_profit}")
    
    # Function to get user input for jobs and processing times
def get_job_input():
    jobs = []
    num_jobs = int(input("Enter the number of jobs: "))

    for i in range(num_jobs):
        job_id = input(f"Enter job ID for Job {i + 1}: ")
        processing_time = int(input(f"Enter processing time for Job {job_id}: "))
        profit = int(input(f"Enter profit for Job {job_id}: "))
        jobs.append([job_id, processing_time, profit])

    return jobs



# Driver's Code
if __name__ == '__main__':
    user_jobs = get_job_input()

    print("Following is the maximum profit sequence of jobs:")
    printJobScheduling(user_jobs, 3)
