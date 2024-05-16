#!/usr/bin/python3
from datetime import datetime
from fabric.api import *

def do_pack():
    """
    Archive all files in web_static
    """

    time = datetime.now()
    archive = 'web_static' + time.strftime("%Y%m%d%H%M%S") + '.tgz'

    local('mkdir -p versions')
    create = local('tar -czvf versions/{} web_static'.format(archive), capture=True)

    if create.succeeded:
        return archive
    else:
        return None
