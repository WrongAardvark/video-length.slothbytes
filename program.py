# take a video's total time "mm:ss" and convert it to seconds.
# if the seconds is above 60 or higher, return -1.


def get_time():

    while True:
        x = input(
            "What's the length of the time of your video? (format should be 'mm:ss') "
        )
        try:
            time_split = x.split(":")

            if int(time_split[1]) < 60:
                total_seconds = int(time_split[0]) * 60 + int(time_split[1])
                print(f"Total seconds: {total_seconds}")
                break
            else:
                print("-1")
                break

        except IndexError:
            print("Please follow the correct time format (mm:ss): ")
        except ValueError:  # noqa: E722
            print("Something went wrong. Try using the correct format (mm:ss): ")


get_time()
