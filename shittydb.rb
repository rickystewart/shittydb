module ShittyDB
  class << self
    def get(key)
      File.read key
    end

    def set(key, value)
      File.write key, value
    end

    def encrypt(key)
      set key, encode(get(key))
    end

    alias decrypt encrypt

    private

    def encode(contents)
      contents.tr 'A-Ma-mN-Zn-z', 'N-Zn-zA-Ma-m'
    end
  end
end
