import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.ZoneOffset;

public class Gigasecond {
    private long epoch;
    private final long gigaSecond = (long) 1e9;
    public Gigasecond(LocalDate moment) {
        this.epoch= moment.atStartOfDay(ZoneOffset.UTC).toEpochSecond();
    }

    public Gigasecond(LocalDateTime moment) {
        this.epoch= moment.atZone(ZoneOffset.UTC).toEpochSecond();
    }

    public LocalDateTime getDateTime() {
        return LocalDateTime.ofEpochSecond(this.epoch + gigaSecond, 0, ZoneOffset.UTC);
    }
}