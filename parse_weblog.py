"""
A module to parse Weblog data and answer interesting questions from the Weblog data.

A line looks like -
201.21.100.64 - - [14/May/2009:05:22:22 -0700] "GET www.twibuzz.com/cgi/tweets.py?q= HTTP/1.1" 200 7481
<client_ip>   I I <time>                        <type> <url>                                   <status_code> <size> <ignore------everything else------->

To parse the file: You will have to tokenize suitably - simplest is to tokenize using <space>.
You can get creative and use Regular Expressions but for simple functions like below,
it is not required.
"""

def unique_ips(filename):
    """
    This function should take a filename as input and *return* all unique client
    IPs from the file, which is a log file from a web server.

    """
    pass

def top_five_urls(filename):
    """
    This function should take a filename and *return* Top 5 URLs.
    Extra Credits. If you write top_n_urls and take howmany top sites to find
    as input
    Hint: Collect data by <url>
    """
    pass

def top_five_client_ips(filename):
    """
    This function takes the filename as input and return top 5 client IPs
    that have downloaded maximum data from the webserver.

    Extra Credits. If you write top_n_clients and take howmany top clients to find
    as input

    Hint: Collect data by <client_ip> and Sum Sizes
    Note: For Status Code 404 when No data transferred is possible, assume 0
    bytes.
    """
    pass

def all_not_found_urls(filename):
    """
    This function takes filename as input and returns all the URLs in the file
    that returned HTTP 404 Status Code.

    Hint: Collect data by <status_code>
    """
    pass

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print ("Usage: python parse_weblog.py <filename>")
        sys.exit(-1)

    filename = sys.argv[1]

    print (unique_ips(filename))
    print (top_five_urls(filename))
    print (top_five_client_ips(filename))
    print (all_not_found_urls(filename))
