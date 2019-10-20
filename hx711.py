# datasheet: https://cdn.sparkfun.com/datasheets/Sensors/ForceFlex/hx711_english.pdf
from gpiozero import AnalogInputDevice, InputDeviceError


class HX711(AnalogInputDevice):
    """
    Extends :class:`AnalogInputDevice` to implement an interface for HX711.
    """

    channel_gain_option = ["A128", "B32", "A64"]
    PD_SCK_PULSES = {"A128": 25, "B32": 26, "A64": 27}

    def __init__(self, bits=24, channel_gain="A128", max_voltage=3.3, **spi_args):
        if channel_gain not in self.channel_gain_option:
            raise InputDeviceError("invalid channel gain options")
        self._min_value = -0x800000
        self._range = 0x7FFFFF - self._min_value  # 0x7FFFFF is max output
        self._sck_pulses = self.PD_SCK_PULSES[channel_gain]
        super().__init__(bits, max_voltage, **spi_args)

    def _read(self):
        return self._words_to_int(self._spi.transfer(self._send())[:-1], self.bits)

    def _send(self):
        """
        From datasheets:
        When output data is not ready for retrieval, digital output pin DOUT is high.
        Serial clock input PD_SCK should be low. When DOUT goes to low, it indicates
        data is ready for retrieval. By applying 25~27 positive clock pulses at the
        PD_SCK pin, data is shifted out from the DOUT output pin. Each PD_SCK pulse
        shifts out one bit, starting with the MSB bit first, until all 24 bits are
        shifted out. The 25th pulse at PD_SCK input will pull DOUT pin back to high.
        """
        return self._int_to_words(2 ** self._sck_pulses - 1)

