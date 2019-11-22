import os
from datetime import datetime


def remove_download_files(downloads, now, retain):
    removed = 0
    total = 0

    print()

    # Go through my downloads and attempt to delete items that are over a certain # of days old
    for file in os.listdir(downloads):
        path = downloads + file

        if os.path.isfile(path) and not file.startswith(".", 0, 1):
            stat = os.stat(path)

            # Can only get birth time on Mac (convenient for me)
            try:
                birth_time_ts = stat.st_birthtime
                birth_time = datetime.fromtimestamp(birth_time_ts)

                diff = now - birth_time

                if diff.days > retain:
                    total += 1

                    while True:
                        will_delete = input("Do you want to delete: {file}? ".format(file=file))
                        will_delete.lower()

                        if will_delete == "yes" or will_delete == "y":
                            os.remove(path)
                            removed += 1
                            break
                        elif will_delete == "no" or will_delete == "n":
                            break
                        else:
                            continue
            except AttributeError:
                print("Oops!")

    print("\n"
          "Removed {removed} files out of {total} eligible files."
          "\n".format(removed=removed, total=total))


def main():
    # Get the downloads folder for the user
    downloads_folder = os.path.expanduser("~/Downloads/")

    # How many days far back should we retain downloads (change to your liking)
    retain = int(input("How far back (in days) do you want to not delete files? "))

    # Get current time
    now = datetime.now()

    remove_download_files(downloads_folder, now, retain)


if __name__ == "__main__":
    main()
