# LIBS
import CloudFlare
import json


# HELPERS
def jprint(arr):
    print(json.dumps(arr, indent=4, sort_keys=False))

# DOCS: https://api.cloudflare.com/
# LIB: https://github.com/cloudflare/python-cloudflare
# NICE EXAMPLES: https://github.com/cloudflare/python-cloudflare/wiki/Examples


class CLOUDFLARE_API(object):

    cf = False
    zones = False
    zone = False
    zone_id = False
    zone_name = False
    domain = False

    def __init__(self, domain, email, token):
        self.domain = domain
        cf = CloudFlare.CloudFlare(email=email, token=token)
        self.cf = cf
        self.zones = cf.zones.get(params={'per_page': 100})

        current_zone = False
        for zone in self.zones:
            if zone['name'] == domain:
                # jprint(zone)
                current_zone = zone

        self.zone = current_zone
        self.zone_id = current_zone['id']
        self.zone_name = current_zone['name']

    def ifNotResticted(self, subdomain):
        if not subdomain:
            return False
        if subdomain.lower() in ['api','www']:
            return False
        return True

    def deleteSubdomain(self, subdomain):

        if self.ifNotResticted(subdomain):

            subdomains = self.cf.zones.dns_records.get(self.zone_id)
            for sub in subdomains:

                matcher = '{}.{}'.format(subdomain, self.domain)
                if sub['name'] == matcher:
                    # jprint(sub)
                    subdomain_dns_record_id = sub['id']

                    self.cf.zones.dns_records.delete(self.zone_id, subdomain_dns_record_id)
                    return True

        return False


    def addSubdomain(self, subdomain):

        if self.ifNotResticted(subdomain):

            dns_record = {'name': subdomain, 'type': 'CNAME', 'content': self.domain}

            # Create DNS record
            try:
                r = self.cf.zones.dns_records.post(self.zone_id, data=dns_record)
            except Exception as e:
                print(e)
                return False

            # Print respose info - they should be the same
            dns_record = r
            dns_record_id = dns_record['id']

            new_dns_record = {
                # Must have type/name/content (even if they don't change)
                'type': dns_record['type'],
                'name': dns_record['name'],
                'content': dns_record['content'],
                # now add new values you want to change
                'proxied': True
            }

            try:
                dns_record = self.cf.zones.dns_records.put(self.zone_id, dns_record_id, data=new_dns_record)
            except Exception as e:
                print(e)
                return False

            return True

        return False



if __name__ == '__main__':
    email = '****'
    token = '****'

    s = CLOUDFLARE_API(domain='estate.im', email=email, token=token).addSubdomain(subdomain='easy')
    # s = CLOUD_FLARE_API(domain='estate.im', email=email, token=token).deleteSubdomain(subdomain='welcomenew')
    print(s)
