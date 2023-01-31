from typing import Any, TextIO

from osdk.model import ComponentManifest, TargetManifest, Props
from osdk.ninja import Writer
from osdk.logger import Logger
from osdk.context import Context, contextFor
from osdk import shell, rules

logger = Logger("builder")


def gen(out: TextIO, context: Context):
    writer = Writer(out)

    target = context.target

    writer.comment("File generated by the build system, do not edit")
    writer.newline()

    writer.separator("Tools")
    for i in target.tools:
        tool = target.tools[i]
        writer.variable(i, tool.cmd)
        writer.variable(
            i + "flags", " ".join(tool.args))
        writer.newline()

    writer.separator("Rules")
    for i in rules.rules:
        tool = target.tools[i]
        rule = rules.rules[i]
        writer.rule(
            i, f"{tool.cmd} {rule.rule.replace('$flags',f'${i}flags')}")
        writer.newline()

    writer.separator("Components")

    for instance in context.instances:
        objects = instance.objsfiles()
        writer.comment(f"Component: {instance.manifest.id}")

        writer.newline()

        for obj in objects:
            r = rules.byFileIn(obj[0])
            if r is None:
                raise Exception(f"Unknown rule for file {obj[0]}")
            writer.build(obj[1], r.id,  obj[0])

        writer.newline()

        if instance.isLib():
            writer.build(instance.libfile(), "ar",
                         list(map(lambda o: o[1], objects)))
        else:
            writer.build(instance.binfile(), "ld",
                         list(map(lambda o: o[1], objects)))

        writer.newline()


def build(componentSpec: str, targetSpec: str = "default",  props: Props = {}) -> str:
    context = contextFor(targetSpec, props)
    target = context.target

    shell.mkdir(target.builddir())
    ninjaPath = f"{target.builddir()}/build.ninja"

    with open(ninjaPath, "w") as f:
        gen(f, context)

    raise NotImplementedError()

    return ""