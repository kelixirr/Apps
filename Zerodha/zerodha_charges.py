import sys
import math

def zerodha_charges(amount, type="delivery", market="NSE", intent="buy"):

    if amount <= 0:
        return "Enter positive investment amount", []

    brokerage = 0
    stamp = 0
    transaction = 0
    stt_ed, stt_id = amount * 0.001, 0
    if intent == "sell":
        stt_id = amount * 0.00025
    if market == "NSE":
        transaction = amount * 0.0000322
    elif market == "BSE":
        transaction = amount * 0.0000375
    else:
        print("Valida Markets: NSE or BSE")

    dp_charges = 13 + 13 * 0.18 if type == "delivery" and intent == "sell" else 0
    if amount >= 10000000:
        sebi = 10 * math.floor(amount / 10000000)
    else:
        sebi = 0

    if type == "intraday":
        brokerage = min(amount * 0.0003, 20)
        stamp = min(amount * 0.00003, 300 * math.floor(amount /
                    10000000)) if intent == "buy" else 0

    elif type == "delivery":
        brokerage = 0
        stamp = min(amount * 0.00015, 1500 *
                    math.floor(amount / 10000000)) if intent == "buy" else 0

    gst = 0.18 * (brokerage + sebi + transaction)
    charges = brokerage + (stt_ed if type == "delivery" else stt_id) + \
        transaction + sebi + stamp + gst + dp_charges
    net = amount - charges

    results = {
        "Brokerage": brokerage,
        "STT/CTT": stt_ed if type == "delivery" else stt_id,
        "DP charges": dp_charges,
        "Transaction charges": transaction,
        "Stamp duty": stamp,
        "SEBI charges": sebi,
        "GST": gst,
        "Net amount": net,
        "Total charges": charges
    }

    if type == "intraday":
        charges_list = [round(brokerage,2), round(transaction, 2), round(stamp, 2), round(stt_id, 2), round(gst, 2), round(sebi, 2)]
    else:
        charges_list = [round(brokerage,2), round(transaction, 2), round(stamp, 2), round(stt_ed, 2), round(gst, 2), round(sebi, 2)]

    return results, charges_list
