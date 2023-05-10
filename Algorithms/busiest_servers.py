class Solution:
    def busiestServers(self, k: int, arrival, load):
        server_load_times = [0] * k
        server_request_count = {i: 0 for i in range(k)}

        def assign_server(desired_server, time, load):
            server = desired_server
            while server_load_times[server] > time:  # this is too slow, need heaps to speed it up

                server = (server + 1) % k
                if server == desired_server: return  # drop this request
            server_load_times[server] = time + load  # sets it to the next time it's free
            server_request_count[server] += 1

        for time in range(len(arrival)):
            load_val = load[time]

            desired_server = time % k
            assign_server(desired_server, time, load_val)

        # Sort the servers by the highest number of requests handled.
        server_request_count = sorted(server_request_count.items(), reverse=True, key=lambda x: x[1])

        # get rid of all server data for non-top servers
        while server_request_count[-1][1] != server_request_count[0][1]:
            server_request_count.pop()
        return [server_request_count[i][0] for i in range(len(server_request_count))]


k = 2
arrival = [1, 4, 5, 7]
load = [3, 2, 7, 8]
s = Solution()
print(s.busiestServers(k, arrival, load))
