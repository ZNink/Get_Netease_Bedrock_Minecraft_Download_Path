#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
获取网易《我的世界》基岩版 7z 直链
"""
import requests
import json

def get_windowsmc_url() -> str:
    """返回官方最新 7z 的直链"""
    url = "https://x19apigatewayobt.nie.netease.com/cpp-game-client-info"
    payload = {"os": "10.0", "version": 100000000, "entity_id": 1}
    headers = {"Content-Type": "application/json"}

    resp = requests.post(url, data=json.dumps(payload), headers=headers, timeout=10)
    resp.raise_for_status()
    return resp.json()["entity"]["url"]

if __name__ == "__main__":
    print(get_windowsmc_url())
