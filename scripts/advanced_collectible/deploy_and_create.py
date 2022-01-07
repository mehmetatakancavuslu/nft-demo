from scripts.helpful_scripts import (
    fund_with_link,
    get_account,
    OPENSEA_URL,
    get_contract,
    config,
)
from brownie import AdvancedCollectible, network


def deploy_and_create():
    account = get_account()
    advanced_colletible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
    )
    fund_with_link(advanced_colletible.address)
    creating_tx = advanced_colletible.createCollectible({"from": account})
    creating_tx.wait(1)
    print("New token has been created!")
    return advanced_colletible, creating_tx


def main():
    deploy_and_create()
