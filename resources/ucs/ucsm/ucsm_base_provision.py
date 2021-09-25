#!/usr/bin/env python3

# Imports
from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.macpool import MacpoolBlock
from ucsmsdk.mometa.uuidpool import UuidpoolBlock
from ucsmsdk.mometa.fabric import FabricEthLan
from ucsmsdk.mometa.fabric import FabricEthLanEp
from ucsmsdk.mometa.ls.LsServer import LsServer
from ucsmsdk.mometa.equipment.EquipmentChassis import EquipmentChassis

# Constants
UCSM = '1.1.1.1'
USER = 'admin'
PW = 'admin'
FABRIC_ID = ['A', 'B']


# Setup UCSM
def setup_ucsm():
    # Perform login
    handle = UcsHandle(
        UCSM,
        USER,
        PW,
        secure=False
    )
    handle.login()

    # Acknowledge Chassis
    mo = EquipmentChassis(
        parent_mo_or_dn='sys',
        admin_state='re-acknowledge',
        handle=5
    )
    handle.add_mo(mo, modify_present=True)

    # Create MAC Pool
    mo = MacpoolBlock(
        parent_mo_or_dn='org-root/mac-pool-default',
        r_from='00:25:B5:00:00:00',
        r_to='00:25:B5:00:00:FF'
    )
    handle.add_mo(mo)

    # Create UUID Pools
    mo = UuidpoolBlock(
        parent_mo_or_dn='org-root/uuid-pool-default',
        r_from='0000-000000000001',
        r_to='0000-000000000099'
    )

    # Setup Ethernet Fabric Sides A & B
    for id in FABRIC_ID:
        mo = FabricEthLan(
            parent_mo_or_dn='fabric/lan',
            id=id
        )
        mo_1 = FabricEthLanEp(
            parent_mo_or_dn=mo,
            admin_speed='10gbps',
            admin_state='enabled',
            auto_negotiate='yes',
            eth_link_profile=''  # Placeholder for value
        )
        handle.add_mo(mo, modify_present=True)

    # Setup Service Profile Template
    mo = LsServer(
        parent_dn_or_mo='org-root',
        ident_pool_name='default',
        name='global_template',
        type='initial-template'
    )
    handle.add_mo(mo)

    # Commit changes to UCSM
    handle.commit()
    handle.logout()
