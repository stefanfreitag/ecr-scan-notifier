import os, sys
import pytest

parent = os.path.abspath("..")
sys.path.insert(1, parent)

import index


def test_ecr_scan_input():
    os.environ["TOPIC_ARN"] = "topic_arn"
    event = {
        "version": "0",
        "id": "822c3bbb-574a-8d0b-828e-b33e93cc0b3a",
        "detail-type": "ECR Image Scan",
        "source": "aws.ecr",
        "account": "012345678912",
        "time": "2022-08-03T18:14:18Z",
        "region": "eu-central-1",
        "resources": ["arn:aws:ecr:eu-central-1:012345678912:repository/sampleapp"],
        "detail": {
            "scan-status": "COMPLETE",
            "repository-name": "sampleapp",
            "image-digest": "sha256:5b5a96370efd56ae20a832244ae56e8e57b1035f493f728eb6cef026586782f7",
            "image-tags": ["3862", "latest"],
            "finding-severity-counts": {
                "HIGH": 3,
                "MEDIUM": 14,
                "INFORMATIONAL": 3,
                "LOW": 1,
                "HIGH": 2,
            },
        },
    }

    output = index.generateEcrScanOutput(event)
    assert "<title>ECR Scan Results</title>" in output


def test_generateInspectorScanOutput():
    event = {
        "version": "0",
        "id": "961d7f4a-f46c-b376-f92f-f8c3af290f9f",
        "detail-type": "Inspector2 Scan",
        "source": "aws.inspector2",
        "account": "520666953574",
        "time": "2022-09-14T19:12:46Z",
        "region": "eu-central-1",
        "resources": ["arn:aws:ecr:eu-central-1:520666953574:repository/azure-agent"],
        "detail": {
            "scan-status": "INITIAL_SCAN_COMPLETE",
            "repository-name": "arn:aws:ecr:eu-central-1:520666953574:repository/azure-agent",
            "finding-severity-counts": {
                "CRITICAL": 0,
                "HIGH": 1,
                "MEDIUM": 6,
                "TOTAL": 10,
            },
            "image-digest": "sha256:734a4d019b381f591a63c819ae88b00eed5dba8b76626530c26497128a6c46d1",
            "image-tags": ["latest", "5715"],
        },
    }
    output = index.generateInspectorScanOutput(event)
    assert "<title>Inspector Scan Results</title>" in output


def test_unsupportedSourceThrowsException():
    os.environ["TOPIC_ARN"] = "topic_arn"

    event = {
        "version": "0",
        "id": "961d7f4a-f46c-b376-f92f-f8c3af290f9f",
        "detail-type": "Inspector2 Scan",
        "source": "unsupported_event",
        "account": "520666953574",
        "time": "2022-09-14T19:12:46Z",
        "region": "eu-central-1",
        "resources": ["arn:aws:ecr:eu-central-1:520666953574:repository/azure-agent"],
        "detail": {
            "scan-status": "INITIAL_SCAN_COMPLETE",
            "repository-name": "arn:aws:ecr:eu-central-1:520666953574:repository/azure-agent",
            "finding-severity-counts": {
                "CRITICAL": 0,
                "HIGH": 1,
                "MEDIUM": 6,
                "TOTAL": 10,
            },
            "image-digest": "sha256:734a4d019b381f591a63c819ae88b00eed5dba8b76626530c26497128a6c46d1",
            "image-tags": ["latest", "5715"],
        },
    }

    with pytest.raises(index.UnsupportedEventException) as exc_info:
        index.handler(event, None)
    assert exc_info.type is index.UnsupportedEventException
    assert exc_info.value.args[0].startswith(
        "Unsupported source or detail-type in event:"
    )
