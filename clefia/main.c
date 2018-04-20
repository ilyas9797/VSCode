#include "clefia_ref.h"

int encrypting(int rounds) {
    FILE *key_f;
    FILE *pts_f;
    FILE *cts_f;

    int err_num = 0;

    // 256-биный ключ
    u8 key[32];
    // 128-битный блок
    u8 pt[16];

    key_f = fopen("samples/key.txt", "rb");
    if (key_f == NULL) {
        printf("Error %d: openning key file", err_num);
        return 1;
    }
    err_num++;

    pts_f = fopen("samples/pts.txt", "rb");
    if (pts_f == NULL) {
        printf("Error %d: openning plain-texts file", err_num);
        return 1;
    }
    err_num++;

    char cts_file_name[10];
    sprintf(cts_file_name, "samples/cts%d.txt", rounds);
    cts_f = fopen(cts_file_name, "wb");
    if (cts_f == NULL) {
        printf("Error %d: openning cipher-texts file", err_num);
        return 1;
    }
    err_num++;

    if (fread(key, sizeof(u8), 32, key_f) != 32) {
            printf("Error %d: reading from key file", err_num);
            return 1;
        }
        err_num++;
    
    int byte_num = 0;
    while ((byte_num = fread(pt, sizeof(u8) , 16, pts_f)) == 16) {

        setup(key);
        crypt(pt, rounds);

        if (fwrite(pt, sizeof(u8), 16, cts_f) != 16){
            printf("Error %d: writing in cipher-texts file", err_num);
            return 1;
        }
        err_num++;
    }
    if (byte_num != 0){
        printf("Error %d: something is wrong with plain-texts file\nbyte_num = %d", err_num, byte_num);
        return 1;
    }
    err_num++;

    fclose(key_f);
    fclose(pts_f);
    fclose(cts_f);

    return 0;
}

int decrypting(int rounds) {
    FILE *key_f;
    FILE *dts_f;
    FILE *cts_f;

    int err_num = 0;

    u8 key[32];
    u8 ct[16];

    key_f = fopen("samples/key.txt", "rb");
    if (key_f == NULL) {
        printf("Error %d: openning key file", err_num);
        return 1;
    }
    err_num++;

    char cts_file_name[10];
    sprintf(cts_file_name, "samples/cts%d.txt", rounds);
    cts_f = fopen(cts_file_name, "rb");
    if (cts_f == NULL) {
        printf("Error %d: openning crypted-texts file", err_num);
        return 1;
    }
    err_num++;

    char dts_file_name[10];
    sprintf(dts_file_name, "samples/dts%d.txt", rounds);
    dts_f = fopen(dts_file_name, "wb");
    if (dts_f == NULL) {
        printf("Error %d: openning decrypted-texts file", err_num);
        return 1;
    }
    err_num++;

    if (fread(key, sizeof(u8), 32, key_f) != 32) {
            printf("Error %d: reading from key file", err_num);
            return 1;
        }
        err_num++;

    int byte_num = 0;
    while ((byte_num = fread(ct, sizeof(u8) , 16, cts_f)) == 16) {

        setup(key);
        decrypt (ct, rounds);

        if (fwrite(ct, sizeof(u8), 16, dts_f) != 16){
            printf("Error %d: writing in decrypted-texts file", err_num);
            return 1;
        }
        err_num++;
    }
    if (byte_num != 0){
        printf("Error %d: something is wrong with plain-texts file\nbyte_num = %d", err_num, byte_num);
        return 1;
    }
    err_num++;

    fclose(key_f);
    fclose(dts_f);
    fclose(cts_f);

    return 0;
}

int main (int argc, char* argv[]) {
    int rounds_start, rounds_end;

    if (argc > 2) {
        rounds_start = (int)atoi(argv[1]);
        rounds_end = (int)atoi(argv[2]);
    }
    else {
        rounds_start = 1;
        rounds_end = 5;
    }

    for (int r = rounds_start; r <= rounds_end; r++) {
        if (encrypting(r) == 1){
            printf("Error with encrypting at %d round\n", r);
            return 1;
        }
    }

    for (int r = rounds_start; r <= rounds_end; r++) {
        if (decrypting(r) == 1){
            printf("Error with decrypting at %d round\n", r);
            return 1;
        }
    }

    return 0;
}