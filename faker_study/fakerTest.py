#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : Lammonx
# @DateTime : 2022/5/8 15:48
from faker.providers import BaseProvider


class P(BaseProvider):

    @staticmethod
    def get_name():
        return Faker(locale='zh_TW').name()


if __name__ == '__main__':
    from faker import Faker

    # f = Faker(locale='zh_CN')
    f = Faker(locale='zh_TW')
    for i in range(10):
        print(f.name(), f.address(), f.job(), f.date_time(), f.company(), f.country())
    # print(f.ipv4_private())
    #
    # from faker import Faker
    # from faker.providers import DynamicProvider
    #
    # medical_professions_provider = DynamicProvider(
    #         provider_name="medical_profession",
    #         elements=["dr.", "doctor", "nurse", "surgeon", "clerk", "你打野"],
    # )
    #
    # fake = Faker(locale='zh_CN')
    #
    # # then add new provider to faker instance
    # fake.add_provider(medical_professions_provider)
    #
    # # now you can use:
    # print(fake.medical_profession())
    # # 'dr.'
    # f = Faker(['zh_CN', 'ja_JP'])
    # for i in range(10):
    #     print(f.name(), f.address(), f.job(), f.date_time(), f.company(), f.country())
    #
    # f = Faker(use_weighting=False)
    # for i in range(10):
    #     print(f.unique.name(), f.address(), f.job(), f.date_time(), f.company(), f.country())
    #
    # f.add_provider(p_1)
    # print(f.get_name())
    # print(f.sentence())
    # print(f.random.getstate())
    # names = [fake.unique.first_name() for i in range(500)]
    # assert len(set(names)) == len(names)
