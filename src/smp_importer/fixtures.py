FIXTURE_1 = """
{
    "@id": "https://openebench.bsc.es/bioschemas/tools/observatory:trimal:1.4/cmd",
    "bioschemas:input": [
        {
            "@type": "https://bioschemas.org/FormatParameter",
            "bioschemas:encodingFormat": " "
        }
    ],    
    "bioschemas:output": [
        {
            "@type": "https://bioschemas.org/FormatParameter",
            "biochemas:encodingFormat": "edam:format_1982"
        },
        {
            "@type": "https://bioschemas.org/FormatParameter",
            "biochemas:encodingFormat": "edam:format_1997"
        },
        {
            "@type": "https://bioschemas.org/FormatParameter",
            "biochemas:encodingFormat": "edam:format_1998"
        },
        {
            "@type": "https://bioschemas.org/FormatParameter",
            "biochemas:encodingFormat": "edam:format_1929"
        },
        {
            "@type": "https://bioschemas.org/FormatParameter",
            "biochemas:encodingFormat": "edam:format_2330"
        }
    ],
    "schema:additionalType": "cmd",
    "schema:applicationCategory": "cmd",
    "schema:applicationSubcategory": [
        "edam:topic_0160",
        "edam:topic_3168",
        "edam:topic_0080"
    ],
    "schema:author": [
        {
            "@type": "https://schema.org/Person",
            "schema:name": "Salvador Capella-Gutierrez"
        }
    ],
    "schema:codeRepository": [
        "https://github.com/scapella/trimal"
    ],
    "schema:dateModified": "10/30/2023T16:10:14Z",
    "schema:description": "Tool for the automated removal of spurious sequences or poorly aligned regions from a multiple sequence alignment.",
    "schema:downloadURL": [
        "https://anaconda.org/bioconda/trimal/1.4.1/download/linux-64/trimal-1.4.1-0.tar.bz2"
    ],
    "schema:featureList": [
        "edam:operation_0492"
    ],
    "schema:license": [
        {
            "@type": "https://schema.org/CreativeWork",
            "schema:name": "GNU General Public License version 2.0 (GPLv2)"
        },
        {
            "@type": "https://schema.org/CreativeWork",
            "schema:name": "GNU General Public License v3 or later (GPLv3+)"
        }
    ],
    "schema:name": "trimal",
    "schema:operatingSystem": [
        "Linux",
        "Windows",
        "macOS"
    ],
    "schema:requirements": [
        "make",
        "compiler_cxx"
    ],
    "schema:softwareHelp": [
        {
            "@id": "http://trimal.cgenomics.org/getting_started_with_trimal_v1.2"
        }
    ],
    "schema:softwareVersion": "1.4",
    "schema:isAccessibleForFree": "true",
    "schema:citation": [
        "https://academic.oup.com/bioinformatics/article/25/15/1972/213148"
    ],
    "schema:discussionURL": [
        "https://github.com/EvaMart/trimal-meta/issues"
    ],
    "schema:usageInfo": [
        "http://trimal.cgenomics.org/getting_started_with_trimal_v1.2"
    ]
}
"""

FIXTURE_2 = """
{
    "@context": {
        "@import": "https://openebench.bsc.es/bioschemas/oebtools.jsonld"
    },
    "@id": "https://openebench.bsc.es/bioschemas/tools/observatory:sentinel-1:None/undefined",
    "@type": "htpps://openebench.bsc.es/bioschemas/oebtools#undefined",
    "schema:additionalType": "undefined",
    "schema:applicationCategory": "undefined",
    "schema:applicationSubcategory": [
        "edam:topic_3837",
        "edam:topic_0102",
        "edam:topic_3050"
    ],
    "schema:author": [
        {
            "@type": "https://schema.org/Person",
            "schema:name": "Soyeon Bae"
        }
    ],
    "schema:dateModified": "10/31/2023T14:11:32Z",
    "schema:description": "Radar vision in the mapping of forest biodiversity from space.",
    "schema:featureList": [
        "edam:operation_3435",
        "edam:operation_2429",
        "edam:operation_2940"
    ],
    "schema:name": "sentinel-1"
}
"""

FIXTURE_3 = """
{
    "@context": {
        "@import": "https://openebench.bsc.es/bioschemas/oebtools.jsonld"
    },
    "@id": "https://openebench.bsc.es/bioschemas/tools/observatory:cutadapt:1.9.1/cmd",
    "@type": "htpps://openebench.bsc.es/bioschemas/oebtools#cmd",
    "bioschemas:input": [
        {
            "@type": "https://bioschemas.org/FormatParameter",
            "biochemas:encodingFormat": "edam:format_1930"
        },
        {
            "@type": "https://bioschemas.org/FormatParameter",
            "biochemas:encodingFormat": "edam:format_1929"
        },
        {
            "@type": "https://bioschemas.org/FormatParameter",
            "biochemas:encodingFormat": "edam:format_1930"
        },
        {
            "@type": "https://bioschemas.org/FormatParameter",
            "biochemas:encodingFormat": "edam:format_1929"
        }
    ],
    "bioschemas:output": [
        {
            "@type": "https://bioschemas.org/FormatParameter",
            "biochemas:encodingFormat": "edam:format_1930"
        },
        {
            "@type": "https://bioschemas.org/FormatParameter",
            "biochemas:encodingFormat": "edam:format_1929"
        },
        {
            "@type": "https://bioschemas.org/FormatParameter",
            "biochemas:encodingFormat": "edam:format_1930"
        },
        {
            "@type": "https://bioschemas.org/FormatParameter",
            "biochemas:encodingFormat": "edam:format_1929"
        }
    ],
    "schema:additionalType": "cmd",
    "schema:applicationCategory": "cmd",
    "schema:applicationSubcategory": [
        "edam:topic_3168",
        "edam:topic_0632",
        "edam:topic_0622"
    ],
    "schema:author": [
        {
            "@type": "https://schema.org/Person",
            "schema:name": "Marcel Martin"
        }
    ],
    "schema:dateModified": "10/31/2023T14:14:21Z",
    "schema:description": "Find and remove adapter sequences, primers, poly-A tails and other types of unwanted sequence from your high-throughput sequencing reads.",
    "schema:downloadURL": [
        "https://anaconda.org/bioconda/cutadapt/1.8.1/download/linux-64/cutadapt-1.8.1-py34_0.tar.bz2",
        "https://pypi.python.org/packages/source/c/cutadapt/cutadapt-1.8.1.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/1.17/download/linux-64/cutadapt-1.17-py35_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.17/download/linux-64/cutadapt-1.17-py36_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.17/download/osx-64/cutadapt-1.17-py35_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.17/download/osx-64/cutadapt-1.17-py36_0.tar.bz2",
        "https://files.pythonhosted.org/packages/27/00/39475c0244d0a99920f461c34632c4f7cbf5544adc4a5addcf6db3c6648c/cutadapt-1.17.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/2.2/download/osx-64/cutadapt-2.2-py37h1de35cc_0.tar.bz2",
        "https://files.pythonhosted.org/packages/6e/78/e14e1b54d1c73634ddbcdb5cc891569419108ee5f597da4a9bad251e5361/cutadapt-2.2.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/1.18/download/linux-64/cutadapt-1.18-py35_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.18/download/linux-64/cutadapt-1.18-py36_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.18/download/osx-64/cutadapt-1.18-py35_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.18/download/osx-64/cutadapt-1.18-py37h1de35cc_1.tar.bz2",
        "https://files.pythonhosted.org/packages/fd/4d/3ac2947d36e2d56ce1513dc4a53d3a45e520d7ccfb43af9ba85408e44c69/cutadapt-1.18.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/2.3/download/osx-64/cutadapt-2.3-py36h1de35cc_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/2.3/download/osx-64/cutadapt-2.3-py37h1de35cc_0.tar.bz2",
        "https://files.pythonhosted.org/packages/b9/21/82fc17e6434e0ee15f24016981fc718fc0b7730f0f849c98879f17d2c1e9/cutadapt-2.3.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/1.13/download/linux-64/cutadapt-1.13-py36_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.13/download/osx-64/cutadapt-1.13-py36_0.tar.bz2",
        "https://pypi.python.org/packages/4b/a0/caf0a418d64a69da12c0f5ede20830f0b7dba2d29efa3f667f1ce69e78da/cutadapt-1.13.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/1.15/download/linux-64/cutadapt-1.15-py35_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.15/download/osx-64/cutadapt-1.15-py35_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.15/download/osx-64/cutadapt-1.15-py36_0.tar.bz2",
        "https://pypi.python.org/packages/5a/89/a041e0a108bef64b1347e9b7126d813e61f0ce028d3db830fb7b77aab1ab/cutadapt-1.15.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/1.16/download/linux-64/cutadapt-1.16-py27_1.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.16/download/linux-64/cutadapt-1.16-py36_1.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.16/download/osx-64/cutadapt-1.16-py36_1.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.16/download/osx-64/cutadapt-1.16-py36_2.tar.bz2",
        "https://pypi.io/packages/source/c/cutadapt/cutadapt-1.16.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/1.11/download/linux-64/cutadapt-1.11-py27_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.11/download/linux-64/cutadapt-1.11-py34_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.11/download/osx-64/cutadapt-1.11-py27_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.11/download/osx-64/cutadapt-1.11-py35_0.tar.bz2",
        "https://pypi.python.org/packages/47/bf/9045e90dac084a90aa2bb72c7d5aadefaea96a5776f445f5b5d9a7a2c78b/cutadapt-1.11.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/2.1/download/osx-64/cutadapt-2.1-py37h1de35cc_0.tar.bz2",
        "https://files.pythonhosted.org/packages/09/2e/60b7747d73d663e49e57244d759fda29778bb00aba172b0753036d1b6b73/cutadapt-2.1.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/1.14/download/linux-64/cutadapt-1.14-py35_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.14/download/linux-64/cutadapt-1.14-py27_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.14/download/linux-64/cutadapt-1.14-py36_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.14/download/osx-64/cutadapt-1.14-py27_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.14/download/osx-64/cutadapt-1.14-py36_0.tar.bz2",
        "https://pypi.python.org/packages/16/e3/06b45eea35359833e7c6fac824b604f1551c2fc7ba0f2bd318d8dd883eb9/cutadapt-1.14.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/2.0/download/osx-64/cutadapt-2.0-py37h1de35cc_0.tar.bz2",
        "https://files.pythonhosted.org/packages/f2/bd/c4054b10cff0a595f6343edf874b98d6bf568703f0bacb0bfd2967ef662a/cutadapt-2.0.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/1.8.3/download/linux-64/cutadapt-1.8.3-py34_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.8.3/download/osx-64/cutadapt-1.8.3-py34_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.8.3/download/osx-64/cutadapt-1.8.3-py35_0.tar.bz2",
        "https://pypi.python.org/packages/source/c/cutadapt/cutadapt-1.8.3.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/2.4/download/osx-64/cutadapt-2.4-py37h1de35cc_0.tar.bz2",
        "https://files.pythonhosted.org/packages/f2/ae/a48f4f4ae8fc1b9660262f6932c43aaa56b55934fa0ced7ee62e66d2d959/cutadapt-2.4.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/1.9.1/download/linux-64/cutadapt-1.9.1-py27_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.9.1/download/linux-64/cutadapt-1.9.1-py35_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.9.1/download/osx-64/cutadapt-1.9.1-py27_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.9.1/download/osx-64/cutadapt-1.9.1-py35_0.tar.bz2",
        "https://pypi.python.org/packages/source/c/cutadapt/cutadapt-1.9.1.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/1.12/download/linux-64/cutadapt-1.12-py35_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.12/download/linux-64/cutadapt-1.12-py27_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.12/download/osx-64/cutadapt-1.12-py35_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.12/download/osx-64/cutadapt-1.12-py34_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/1.12/download/osx-64/cutadapt-1.12-py35_1.tar.bz2",
        "https://pypi.python.org/packages/41/9e/5b673f766dcf2dd787e0e6c9f08c4eea6f344ea8fce824241db93cc2175f/cutadapt-1.12.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/2.5/download/osx-64/cutadapt-2.5-py37h01d97ff_0.tar.bz2",
        "https://files.pythonhosted.org/packages/82/32/20742c90e86ac605c43b8ea3789966413d381bc4e80c712691f84ff3fb7c/cutadapt-2.5.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/2.6/download/osx-64/cutadapt-2.6-py37h01d97ff_0.tar.bz2",
        "https://files.pythonhosted.org/packages/51/b3/e39f0b90dc3a4a96e73e0a2ad8249e09cde7310ad2f89f55616861edca31/cutadapt-2.6.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/2.7/download/osx-64/cutadapt-2.7-py37h01d97ff_0.tar.bz2",
        "https://files.pythonhosted.org/packages/ef/af/884ff2b7db07eed505b19361402782ae68c827f3aa2e221710a42363cf91/cutadapt-2.7.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/2.8/download/osx-64/cutadapt-2.8-py37h01d97ff_0.tar.bz2",
        "https://files.pythonhosted.org/packages/94/e2/de61c38fbe04933045287fc27bfb56eebc388b16ee8e815ef6bf9f68b4ad/cutadapt-2.8.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/2.9/download/osx-64/cutadapt-2.9-py37h01d97ff_0.tar.bz2",
        "https://files.pythonhosted.org/packages/07/fb/416956d0c5a1949b97b3859933c5e9a8a0922a8daa33507486a2f510662a/cutadapt-2.9.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/2.10/download/osx-64/cutadapt-2.10-py37h01d97ff_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/2.10/download/osx-64/cutadapt-2.10-py37hea0d0e9_1.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/2.10/download/osx-64/cutadapt-2.10-py38h771b250_1.tar.bz2",
        "https://files.pythonhosted.org/packages/4b/9d/3f98c2619206430ad11e485a2a2f6b3e37f792f11523fee372739abdc1cd/cutadapt-2.10.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/3.0/download/osx-64/cutadapt-3.0-py38h771b250_0.tar.bz2",
        "https://files.pythonhosted.org/packages/a5/e9/d259b36c180e43f4a69146aad569220034c98a8830dfcf27723818ae173d/cutadapt-3.0.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/3.1/download/osx-64/cutadapt-3.1-py38h771b250_0.tar.bz2",
        "https://files.pythonhosted.org/packages/1e/22/71634e9a05a6fd136e1da45c8e4c38ba87997b7c1b24a2c6e4acd7b12542/cutadapt-3.1.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/3.2/download/osx-64/cutadapt-3.2-py38h771b250_0.tar.bz2",
        "https://files.pythonhosted.org/packages/c2/e4/2139a7bc387407392e3a2bb5e903f4369bf55bbb6578fb5411f7cfd65c10/cutadapt-3.2.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/3.3/download/osx-64/cutadapt-3.3-py38h771b250_0.tar.bz2",
        "https://files.pythonhosted.org/packages/6a/86/281aa1be72783304dae326c45b03bca0e1561dcc0e5f37c99012f622df72/cutadapt-3.3.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/3.4/download/osx-64/cutadapt-3.4-py38h771b250_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/3.4/download/osx-64/cutadapt-3.4-py39ha492530_1.tar.bz2",
        "https://files.pythonhosted.org/packages/2f/02/f7550d8f1f53690d0812242800ed0f1f847945d07c0749f830a5f52c79ee/cutadapt-3.4.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/3.5/download/osx-64/cutadapt-3.5-py39ha492530_0.tar.bz2",
        "https://files.pythonhosted.org/packages/46/b5/853d2049f975ae1fec3149acf48aa635fdb022192e9db9470f9bb3bbb777/cutadapt-3.5.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/3.6/download/osx-64/cutadapt-3.6-py39h7222f55_0.tar.bz2",
        "https://files.pythonhosted.org/packages/b1/4e/4a65ccb74c5726aad123bfb80def51bd136b346b3e842356bdb6808c6457/cutadapt-3.6.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/3.7/download/osx-64/cutadapt-3.7-py39h7222f55_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/3.7/download/osx-64/cutadapt-3.7-py39h7222f55_1.tar.bz2",
        "https://files.pythonhosted.org/packages/c3/b2/28aa2c570d5f184de0086171d1f25fab1d34224c59806d941779fff6f26b/cutadapt-3.7.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/4.0/download/osx-64/cutadapt-4.0-py39h7222f55_0.tar.bz2",
        "https://files.pythonhosted.org/packages/c2/6e/f9d9671f2e5ee8683d6fc709eaf2184b05d8adc4861b41ac87133a5c23d2/cutadapt-4.0.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/4.1/download/osx-64/cutadapt-4.1-py39h7222f55_0.tar.bz2",
        "https://anaconda.org/bioconda/cutadapt/4.1/download/osx-64/cutadapt-4.1-py39h7222f55_1.tar.bz2",
        "https://files.pythonhosted.org/packages/a3/30/4a889a6916d7480c153774777e634b89865f95cb02f2c3209762c7ef984b/cutadapt-4.1.tar.gz",
        "https://anaconda.org/bioconda/cutadapt/4.2/download/osx-64/cutadapt-4.2-py39h2c9d64e_0.tar.bz2",
        "https://files.pythonhosted.org/packages/45/20/7e4d6ebfa2826ff2823e92113c4f7d3502ea0d9a70a5df614a22863edffd/cutadapt-4.2.tar.gz",
        "https://files.pythonhosted.org/packages/45/20/7e4d6ebfa2826ff2823e92113c4f7d3502ea0d9a70a5df614a22863edffd/cutadapt-4.2.tar.gz",
        "https://files.pythonhosted.org/packages/45/20/7e4d6ebfa2826ff2823e92113c4f7d3502ea0d9a70a5df614a22863edffd/cutadapt-4.2.tar.gz"
    ],
    "schema:featureList": [
        "edam:operation_3695",
        "edam:operation_2403",
        "edam:operation_0369",
        "edam:operation_3192"
    ],
    "schema:license": [
        {
            "@type": "https://schema.org/CreativeWork",
            "schema:name": "MIT"
        }
    ],
    "schema:name": "cutadapt",
    "schema:operatingSystem": [
        "Linux",
        "Windows",
        "macOS"
    ],
    "schema:requirements": [
        "cutadapt/1.6",
        "compiler_c",
        "pip",
        "python",
        "cython",
        "setuptools-scm",
        "xopen >=1.6.0",
        "dnaio >=0.9.1",
        "dataclasses >=0.7"
    ],
    "schema:softwareHelp": [
        {
            "@id": "https://cutadapt.readthedocs.io/en/stable/"
        }
    ],
    "schema:softwareVersion": "1.9.1"
}
"""
