# Regression test: a `# fmt: skip` right after an opening parenthesis preserves
# the parenthesized group verbatim. When more tokens of the same statement
# follow the group (the `in ...` of a `for` header, an `as` clause, a trailing
# operator, ...), formatting the remainder on its own used to produce
# unparseable output. The whole statement is now preserved instead.

if (some_long_condition  # fmt: skip
        and another):
    pass

for (  # fmt: skip
    a,
    b,
) in c:
    pass

with (  # fmt: skip
    open("a")
) as f:
    pass

try:
    pass
except (  # fmt: skip
    ValueError
) as e:
    pass

if (  # fmt: skip
    a
) and b:
    pass

x = (  # fmt: skip
    1
) + 2

for (  # fmt: skip
    a,
    b,
) in c:
    x=1


async def f():
    async for (  # fmt: skip
        a,
        b,
    ) in c:
        pass


def g():
    for (  # fmt: skip
        a,
        b,
    ) in c:
        pass
