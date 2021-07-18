import speedtest
test = speedtest.Speedtest()

print("Loading server list...")
test.get_servers()
print("Choosing best server...")
best = test.get_best_server()
print(f"Found: {best['host']} located in {best['country']}")


print("Performing download test...")
download_speed = test.download()


print("Performing upload test...")
upload_speed = test.upload()


ping_result = test.results.ping


print(f" Download_speed: {download_speed / 1024 /1024:.2f} Mbit/s")
print(f" Uplaod_speed: {upload_speed / 1024 / 1024:.2f} Mbit/s")
print(f" Ping: {ping_result:.2f} ms")