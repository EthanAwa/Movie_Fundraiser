print("Hello, World!")
for i in range(0, 100, 5):
    print(i)

engineer = input("building: ").lower().strip()

if engineer != "sentry" and engineer != "minisentry":
    print("sap")
else:
    print("shoot gun")