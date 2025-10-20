from __future__ import annotations
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
import os


def init_telemetry(app: FastAPI) -> None:
    # Prometheus metrics
    Instrumentator().instrument(app).expose(app, endpoint="/metrics")

    # OpenTelemetry traces
    service_name = os.getenv("OTEL_SERVICE_NAME", "social-media-backend")
    otlp_endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT")

    resource = Resource.create({"service.name": service_name})
    provider = TracerProvider(resource=resource)
    trace.set_tracer_provider(provider)

    if otlp_endpoint:
        exporter = OTLPSpanExporter(endpoint=otlp_endpoint)
        processor = BatchSpanProcessor(exporter)
        provider.add_span_processor(processor)

    FastAPIInstrumentor.instrument_app(app)
