#!/usr/bin/env python3

# Imports
from ucsmsdk.ucshandle import UcsHandle
from random import randint

# Constants
UCSM = '1.1.1.1'
USER = 'admin'
PWD = 'admin'


# Login
def login():
    handle = UcsHandle(
        UCSM,
        USER,
        PWD,
        secure=False
    )

    handle.login()
    print('\n** Login Successful **\n')
    return handle


# Logout
def logout(handle):
    handle.logout()
    print('\n** Logout Successful **')


# Get blades by class
def get_blades_by_class(handle):
    blades = handle.query_classid('computeBlade')

    for blade in blades:
        print(blade.dn, blade.name, blade.model)


# Get blades by class with a filter
def get_blades_by_class_with_filter(handle, filter=None):
    if filter is not None:
        filter = "('model', 'UCSB-EX-M4-1, type='eq')"

    blades = handle.query_classid('computeBlade', filter_str=filter)
    for blade in blades:
        print(blade.dn, blade.name, blade.model)


# Get a blade by DN
def get_blade_by_dn(handle):
    # Create a data set of blades
    blades = handle.query_classid('computeBlade')

    blades_len = randint(0, len(blades))
    blade_choice = blades[blades_len]

    blade_dn = handle.query_dn(blades[blade_choice].dn)

    print(blade_dn)


# Create a VLAN
def create_vlan(handle, id='100'):
    # Import the FabricVlan class
    from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

    # Create parent managed object
    lan_clouds = handle.query_classid('FabricLanCloud')
    lan_cloud_mo = lan_clouds[0]

    # Create a VLAN managed object
    vlan_mo = FabricVlan(
        parent_mo_or_dn=lan_cloud_mo,
        name=f'vlan{str(id)}',
        id=str(id)
    )

    # Add the VLAN managed object to the handle
    handle.addMo = vlan_mo

    # Commit the change
    handle.commit()


# Update a VLAN
def update_vlan(handle, id='100'):
    # Create a managed object for the VLAN
    vlan_100_mo = handle.query_dn('fabric/lan/net-vlan100')
    print(vlan_100_mo.dn, vlan_100_mo.sharing)

    # Set the attribute(s) to update
    vlan_100_mo.sharing = 'primary'

    # Add the VLAN managed object to the handle
    handle.set_mo(vlan_100_mo)

    # Commit the change
    handle.commit()

    # Get updated VLAN details
    vlan_100a_mo = handle.query_dn('fabric/lan/net-vlan100')
    print(vlan_100a_mo.dn, vlan_100a_mo.sharing)


# Delete a vlan
def delete_vlan(handle, id='100'):
    # Create a managed object for the VLAN
    vlan_100_mo = handle.query_dn('fabric/lan/net-vlan100')

    # Mark the managed object for delete in the handle
    handle.remove_mo(vlan_100_mo)

    # Commit the delete
    handle.commit()
