"""Tests for the iso_container package."""
import pytest

from iso_container import get_container_info, validate_container


class TestValidateContainer:
    @pytest.mark.parametrize('number', [
        'CSQU3054383',  # canonical ISO 6346 example
        'MSCU1234566',
        'HLCU8765437',
        'TCLU7654320',  # check digit computed as 0
        'csqu3054383',  # lowercase is normalized before validation
    ])
    def test_valid_numbers(self, number):
        assert validate_container(number) is True

    @pytest.mark.parametrize('number', [
        'CSQU3054384',  # valid prefix, wrong check digit
        'MSCU1234567',
        'HLCU8765438',
    ])
    def test_wrong_check_digit(self, number):
        assert validate_container(number) is False

    @pytest.mark.parametrize('number', [
        '',              # empty
        'CSQU305438',    # 10 chars, too short
        'CSQU30543833',  # 12 chars, too long
    ])
    def test_wrong_length(self, number):
        assert validate_container(number) is False

    @pytest.mark.parametrize('number', [
        'CSQ13054383',  # digit in the owner/category block
        'CSQU30543U3',  # letter in the serial block
        'CSQU305438A',  # non-digit check digit
    ])
    def test_wrong_format(self, number):
        assert validate_container(number) is False

    @pytest.mark.parametrize('number', [
        'ÄBCU1234567',  # non-ASCII letter (isalpha() is True) — regression
        'ABCU²²²²²²²',  # non-ASCII digit (isdigit() is True) — regression
    ])
    def test_non_ascii_returns_false_not_crash(self, number):
        """Regression: these used to raise TypeError/ValueError instead of returning False."""
        assert validate_container(number) is False

    @pytest.mark.parametrize('number', [f'ABCU000007{d}' for d in '0123456789'])
    def test_remainder_10_prefix_is_always_invalid(self, number):
        # ISO 6346: a prefix whose checksum remainder is 10 has no valid check digit.
        assert validate_container(number) is False

    def test_whitespace_is_not_stripped(self):
        # Input is not normalized; spaced numbers are rejected by design.
        assert validate_container('CSQU 3054383') is False


class TestGetContainerInfo:
    def test_known_code_returns_info(self):
        info = get_container_info('22GP')
        assert info is not None
        assert set(info) == {'class', 'type', 'length', 'height'}

    def test_known_code_returns_expected_values(self):
        info = get_container_info('22GP')
        assert info['length'] == 20
        assert info['height'] == 8.5

    def test_unknown_code_returns_none(self):
        assert get_container_info('ZZZZ') is None

    def test_lookup_is_case_insensitive(self):
        # Codes are stored uppercase; input is normalized before lookup.
        assert get_container_info('22gp') == get_container_info('22GP')
