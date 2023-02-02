# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2023.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Examples for EnterpriseBillingUnitsV1
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
import os
import pytest
import json
from ibm_platform_services.enterprise_billing_units_v1 import *

#
# This file provides an example of how to use the Enterprise Billing Units service.
#
# The following configuration properties are assumed to be defined:
#
# ENTERPRISE_BILLING_UNITS_URL=<service url>
# ENTERPRISE_BILLING_UNITS_AUTHTYPE=iam
# ENTERPRISE_BILLING_UNITS_APIKEY=<your iam apikey>
# ENTERPRISE_BILLING_UNITS_AUTH_URL=<IAM token service URL - omit this if using the production environment>
# ENTERPRISE_BILLING_UNITS_ENTERPRISE_ID=<id of enterprise to use for examples>
# ENTERPRISE_BILLING_UNITS_BILLING_UNIT_ID=<id of billing unit to use for examples>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'enterprise_billing_units.env'

enterprise_billing_units_service = None

config = None


##############################################################################
# Start of Examples for Service: EnterpriseBillingUnitsV1
##############################################################################
# region
class TestEnterpriseBillingUnitsV1Examples:
    """
    Example Test Class for EnterpriseBillingUnitsV1
    """

    @classmethod
    def setup_class(cls):
        global enterprise_billing_units_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            enterprise_billing_units_service = EnterpriseBillingUnitsV1.new_instance()

            # end-common
            assert enterprise_billing_units_service is not None

            # Load the configuration

            global config, enterprise_id, billing_unit_id
            config = read_external_sources(EnterpriseBillingUnitsV1.DEFAULT_SERVICE_NAME)

            enterprise_id = config['ENTERPRISE_ID']
            billing_unit_id = config['BILLING_UNIT_ID']

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_get_billing_unit_example(self):
        """
        get_billing_unit request example
        """
        try:
            global billing_unit_id
            print('\nget_billing_unit() result:')

            # begin-get_billing_unit

            billing_unit = enterprise_billing_units_service.get_billing_unit(
                billing_unit_id=billing_unit_id
            ).get_result()

            print(json.dumps(billing_unit, indent=2))

            # end-get_billing_unit

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_billing_units_example(self):
        """
        list_billing_units request example
        """
        try:
            global enterprise_id
            print('\nlist_billing_units() result:')
            # begin-list_billing_units

            all_results = []
            pager = BillingUnitsPager(
                client=enterprise_billing_units_service,
                enterprise_id=enterprise_id,
                limit=10,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_billing_units

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_billing_options_example(self):
        """
        list_billing_options request example
        """
        try:
            global billing_unit_id
            print('\nlist_billing_options() result:')
            # begin-list_billing_options

            all_results = []
            pager = BillingOptionsPager(
                client=enterprise_billing_units_service,
                billing_unit_id=billing_unit_id,
                limit=10,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_billing_options

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_credit_pools_example(self):
        """
        get_credit_pools request example
        """
        try:
            global billing_unit_id
            print('\nget_credit_pools() result:')

            # begin-get_credit_pools

            all_results = []
            pager = GetCreditPoolsPager(
                client=enterprise_billing_units_service,
                billing_unit_id=billing_unit_id,
                type='PLATFORM',
                limit=10,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-get_credit_pools
        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: EnterpriseBillingUnitsV1
##############################################################################
