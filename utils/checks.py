from discord import Member
from discord.ext.commands import check

from bot.config import settings


def is_admin(member: Member):
    return any(
        role.id in settings.moderation.admin_roles_ids for role in member.roles
    )


def is_staff(member: Member):
    return any(
        role.id == settings.moderation.staff_role_id for role in member.roles
    )


def is_engineer(member: Member):
    for role in member.roles:
        if role.id == settings.tags.required_role_id:
            return True

    return is_staff(member)


def is_staff_check():
    def predicate(ctx):
        return is_staff(ctx.author)

    return check(predicate)


def is_engineer_check():
    def predicate(ctx):
        return is_engineer(ctx.author)

    return check(predicate)


def in_twt():
    def predicate(ctx):
        return ctx.guild.id == settings.guild.id

    return check(predicate)
