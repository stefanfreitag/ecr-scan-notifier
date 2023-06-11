import json
import os
import sys
import logging
import boto3
from jinja2 import Environment, FileSystemLoader, select_autoescape


logging.basicConfig(stream=sys.stdout, level=logging.INFO)
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


class UnsupportedEventException(Exception):
    """Exception raised when an supported event is detected."""


def handler(event, context):
    """handler function"""
    topic_arn = os.environ["TOPIC_ARN"]

    if (
        event["source"] == "aws.inspector2"
        and event["detail-type"] == "Inspector2 Scan"
    ):

        rendered_template = generateInspectorScanOutput(event)
        publish(topic_arn, rendered_template, "AWS Inspector Scan")

    elif event["source"] == "aws.ecr" and event["detail-type"] == "ECR Image Scan":
        rendered_template = generateEcrScanOutput(event)
        publish(topic_arn, rendered_template, "ECR Image Scan")
    else:
        raise UnsupportedEventException(
            "Unsupported source or detail-type in event:" + str(event)
        )


def publish(topic_arn, rendered_template: str, title: str):
    client = boto3.client("sns")
    client.publish(
        TargetArn=topic_arn,
        Message=json.dumps({"default": rendered_template}),
        Subject=title,
        MessageStructure="json",
    )


def generateEcrScanOutput(event):
    env = Environment(
        autoescape=select_autoescape(),
        loader=FileSystemLoader([os.path.join(os.path.dirname(__file__), "templates")]),
    )

    template = env.get_template("ecr_scan_result.html")
    template_input = {}
    template_input["account"] = event["account"]
    template_input["scanned_at"] = event["time"]
    template_input["image_tags"] = event["detail"]["image-tags"]
    template_input["scan_status"] = event["detail"]["scan-status"]
    template_input["repository_name"] = event["detail"]["repository-name"]
    template_input["findings_critical"] = (
        event["detail"]["finding-severity-counts"]["CRITICAL"]
        if "CRITICAL" in event["detail"]["finding-severity-counts"]
        else 0
    )
    template_input["findings_high"] = (
        event["detail"]["finding-severity-counts"]["HIGH"]
        if "HIGH" in event["detail"]["finding-severity-counts"]
        else 0
    )
    template_input["findings_medium"] = (
        event["detail"]["finding-severity-counts"]["MEDIUM"]
        if "MEDIUM" in event["detail"]["finding-severity-counts"]
        else 0
    )
    template_input["findings_low"] = (
        event["detail"]["finding-severity-counts"]["LOW"]
        if "LOW" in event["detail"]["finding-severity-counts"]
        else 0
    )
    template_input["findings_informational"] = (
        event["detail"]["finding-severity-counts"]["INFORMATIONAL"]
        if "INFORMATIONAL" in event["detail"]["finding-severity-counts"]
        else 0
    )

    template_input["findings_undefined"] = (
        event["detail"]["finding-severity-counts"]["UNDEFINED"]
        if "UNDEFINED" in event["detail"]["finding-severity-counts"]
        else 0
    )

    rendered_template = template.render(template_input)
    return rendered_template


def generateInspectorScanOutput(event):
    env = Environment(
        autoescape=select_autoescape(),
        loader=FileSystemLoader([os.path.join(os.path.dirname(__file__), "templates")]),
    )

    template = env.get_template("inspector_scan_result.html")
    template_input = {}
    template_input["account"] = event["account"]
    template_input["scanned_at"] = event["time"]
    template_input["image_tags"] = event["detail"]["image-tags"]
    template_input["scan_status"] = event["detail"]["scan-status"]
    template_input["repository_name"] = event["detail"]["repository-name"]
    template_input["findings_critical"] = (
        event["detail"]["finding-severity-counts"]["CRITICAL"]
        if "CRITICAL" in event["detail"]["finding-severity-counts"]
        else 0
    )
    template_input["findings_high"] = (
        event["detail"]["finding-severity-counts"]["HIGH"]
        if "HIGH" in event["detail"]["finding-severity-counts"]
        else 0
    )
    template_input["findings_medium"] = (
        event["detail"]["finding-severity-counts"]["MEDIUM"]
        if "MEDIUM" in event["detail"]["finding-severity-counts"]
        else 0
    )
    template_input["findings_low"] = (
        event["detail"]["finding-severity-counts"]["LOW"]
        if "LOW" in event["detail"]["finding-severity-counts"]
        else 0
    )
    template_input["findings_undefined"] = (
        event["detail"]["finding-severity-counts"]["UNDEFINED"]
        if "UNDEFINED" in event["detail"]["finding-severity-counts"]
        else 0
    )

    template_input["findings_total"] = (
        event["detail"]["finding-severity-counts"]["TOTAL"]
        if "TOTAL" in event["detail"]["finding-severity-counts"]
        else 0
    )
    rendered_template = template.render(template_input)
    return rendered_template
