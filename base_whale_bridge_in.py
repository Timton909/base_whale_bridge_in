import requests, time

def bridge_in():
    print("Base — Whale Bridge In (> $500k from Ethereum L1)")
    seen = set()

    while True:
        try:
            # Official Base bridge contract on Ethereum side
            r = requests.get("https://api.etherscan.io/api?module=account&action=txlist"
                             "&address=0x49048044D57e1C92A77f79988d21Fa8fAF74E97e&sort=desc")
            for tx in r.json().get("result", [])[:30]:
                h = tx["hash"]
                if h in seen: continue
                seen.add(h)

                if "0x3154cf16" not in tx.get("input", "")[:10]: continue  # depositTransaction selector

                value = int(tx["value"]) / 1e18
                if value >= 500_000:  # > $500k entering Base
                    print(f"WHALE BRIDGE IN\n"
                          f"${value:,.0f} entering Base from L1\n"
                          f"Wallet: {tx['from'][:10]}...\n"
                          f"Tx: https://etherscan.io/tx/{h}\n"
                          f"→ Fresh money hitting Base — liquidity incoming\n"
                          f"{'BRIDGE IN'*15}")

        except:
            pass
        time.sleep(4.2)

if __name__ == "__main__":
    bridge_in()
